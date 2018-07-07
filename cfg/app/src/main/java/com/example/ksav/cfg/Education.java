package com.example.ksav.cfg;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

public class Education extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_education);

    }
    public void toMainActivity(View view){
        Toast.makeText(this,"Form submitted successfully",Toast.LENGTH_SHORT).show();
        Intent toMainActivity = new Intent(this,MainActivity.class);
        startActivity(toMainActivity);
    }
}
