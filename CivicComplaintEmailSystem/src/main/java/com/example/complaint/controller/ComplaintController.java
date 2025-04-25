import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.mail.MessagingException;

@RestController
@RequestMapping("/complaint")
public class ComplaintController {

    @Autowired
    private EmailService emailService;

    @PostMapping("/submit")
    public String submitComplaint(@RequestBody Complaint complaint) {
        // Logic to save the complaint in the database (already implemented in your backend)
        
        // After saving, send email
        try {
            String subject = "New Complaint Submitted: " + complaint.getCategory();
            String body = "Complaint Details:\n" +
                          "Location: " + complaint.getLocation() + "\n" +
                          "Category: " + complaint.getCategory() + "\n" +
                          "Description: " + complaint.getDescription() + "\n" +
                          "Image: " + complaint.getImageUrl(); // Add image URL if necessary
            
            // Sending email (email address can be dynamic depending on department, for now, sending to a fixed email)
            emailService.sendEmail("manojbabu.ch22@gmail.com", subject, body);
            
        } catch (MessagingException e) {
            e.printStackTrace();
            return "Error in sending email.";
        }

        return "Complaint submitted successfully!";
    }
}
