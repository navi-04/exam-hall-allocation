import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.io.File;
import java.io.FileInputStream;
import java.sql.*;
import java.util.Vector;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import com.twilio.Twilio;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;

public class AttendanceTracker extends JFrame {
    // Twilio credentials - replace with your actual credentials
    private static final String ACCOUNT_SID = "";
    private static final String AUTH_TOKEN = "";
    private static final String TWILIO_PHONE = "";
    
    private JTable table;
    private JButton loadButton;
    private JButton calculateButton;
    private Connection conn;
    
    public AttendanceTracker() {
        setTitle("Student Attendance Tracker");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // Initialize database
        initializeDB();
        
        // Create UI components
        table = new JTable();
        JScrollPane scrollPane = new JScrollPane(table);
        
        loadButton = new JButton("Load Excel");
        calculateButton = new JButton("Calculate Attendance");
        
        // Layout
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(loadButton);
        buttonPanel.add(calculateButton);
        
        setLayout(new BorderLayout());
        add(buttonPanel, BorderLayout.NORTH);
        add(scrollPane, BorderLayout.CENTER);
        
        // Add action listeners
        loadButton.addActionListener(e -> loadExcelFile());
        calculateButton.addActionListener(e -> calculateAttendance());
    }
    
    private void initializeDB() {
        try {
            Class.forName("org.sqlite.JDBC");
            conn = DriverManager.getConnection("jdbc:sqlite:attendance.db");
            Statement stmt = conn.createStatement();
            stmt.execute("CREATE TABLE IF NOT EXISTS attendance (" +
                        "student_name TEXT, " +
                        "phone_number TEXT, " +
                        "attendance_percentage REAL)");
        } catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Database initialization failed: " + e.getMessage());
        }
    }
    
    private void loadExcelFile() {
        JFileChooser fileChooser = new JFileChooser();
        if (fileChooser.showOpenDialog(this) == JFileChooser.APPROVE_OPTION) {
            try {
                File file = fileChooser.getSelectedFile();
                FileInputStream fis = new FileInputStream(file);
                Workbook workbook = new XSSFWorkbook(fis);
                Sheet sheet = workbook.getSheetAt(0);
                
                // Create table model
                DefaultTableModel model = new DefaultTableModel();
                Row headerRow = sheet.getRow(0);
                
                // Add columns to model
                for (Cell cell : headerRow) {
                    model.addColumn(cell.getStringCellValue());
                }
                
                // Add data rows
                for (int i = 1; i <= sheet.getLastRowNum(); i++) {
                    Row row = sheet.getRow(i);
                    Vector<Object> data = new Vector<>();
                    for (Cell cell : row) {
                        switch (cell.getCellType()) {
                            case STRING:
                                data.add(cell.getStringCellValue());
                                break;
                            case NUMERIC:
                                data.add(cell.getNumericCellValue());
                                break;
                            default:
                                data.add("");
                        }
                    }
                    model.addRow(data);
                }
                
                table.setModel(model);
                workbook.close();
                fis.close();
                
            } catch (Exception e) {
                e.printStackTrace();
                JOptionPane.showMessageDialog(this, "Error loading Excel file: " + e.getMessage());
            }
        }
    }
    
    private void calculateAttendance() {
        DefaultTableModel model = (DefaultTableModel) table.getModel();
        int rowCount = model.getRowCount();
        int dateColumns = model.getColumnCount() - 2; // Subtract name and phone columns
        
        try {
            PreparedStatement pstmt = conn.prepareStatement(
                "INSERT OR REPLACE INTO attendance (student_name, phone_number, attendance_percentage) VALUES (?, ?, ?)");
                
            for (int i = 0; i < rowCount; i++) {
                String studentName = model.getValueAt(i, 0).toString();
                String phoneNumber = model.getValueAt(i, model.getColumnCount() - 1).toString();
                
                // Calculate attendance
                int presentCount = 0;
                for (int j = 1; j < dateColumns; j++) {
                    String attendance = model.getValueAt(i, j).toString().toLowerCase();
                    if (attendance.equals("present")) {
                        presentCount++;
                    }
                }
                
                double attendancePercentage = (double) presentCount / (dateColumns - 1) * 100;
                
                // Store in database
                pstmt.setString(1, studentName);
                pstmt.setString(2, phoneNumber);
                pstmt.setDouble(3, attendancePercentage);
                pstmt.executeUpdate();
                
                // Send SMS if attendance is below 80%
                if (attendancePercentage < 80) {
                    sendSMS(phoneNumber, studentName, attendancePercentage);
                }
            }
            
            JOptionPane.showMessageDialog(this, "Attendance calculated and stored successfully!");
            
        } catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Error calculating attendance: " + e.getMessage());
        }
    }
    
    private void sendSMS(String phoneNumber, String studentName, double attendance) {
        try {
            Twilio.init(ACCOUNT_SID, AUTH_TOKEN);
            Message message = Message.creator(
                new PhoneNumber(phoneNumber),
                new PhoneNumber(TWILIO_PHONE),
                "Dear " + studentName + ", your attendance is " + String.format("%.2f", attendance) + 
                "% which is below the required 80%. Please improve your attendance."
            ).create();
            
            System.out.println("SMS sent: " + message.getSid());
        } catch (Exception e) {
            e.printStackTrace();
            System.err.println("Failed to send SMS to " + phoneNumber + ": " + e.getMessage());
        }
    }
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            AttendanceTracker tracker = new AttendanceTracker();
            tracker.setVisible(true);
        });
    }
}