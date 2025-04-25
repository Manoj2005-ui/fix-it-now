
package com.example.complaint.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

@Service
public class EmailServiceImpl implements EmailService {

    @Autowired
    private JavaMailSender mailSender;

    @Override
    public void sendEmail(String to, String subject, String text) {
        SimpleMailMessage msg = new SimpleMailMessage();
        msg.setFrom("manojbabu.ch22@gmail.com"); // Replace with your email
        msg.setTo(to);
        msg.setSubject(subject);
        msg.setText(text);
        mailSender.send(msg);
    }
}
