package com.example.message;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;
import com.samsao.messageui.views.MessagesWindow;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        if (! Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }
        final MessagesWindow messageswindow = (MessagesWindow) findViewById(R.id.customized_messages_window);
        final EditText message = messageswindow.getWritingMessageView().findViewById(com.samsao.messageui.R.id.message_box_text_field);
        message.setHint("Type here ...");
        messageswindow.setBackgroundResource(R.color.colorPrimaryDark);
        messageswindow.receiveMessage("Hi, Welcome to Chatbot for E-commerce.");
        messageswindow.receiveMessage("My name is EDITH");
        messageswindow.getWritingMessageView().findViewById(com.samsao.messageui.R.id.message_box_button).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Python py = Python.getInstance();
                messageswindow.sendMessage(message.getText().toString());
                PyObject pyobj = py.getModule("script");
                PyObject obj = pyobj.callAttr("main",message.getText().toString().toLowerCase());
                message.setText("");
                messageswindow.receiveMessage(obj.toString());
            }
        });
    }
}