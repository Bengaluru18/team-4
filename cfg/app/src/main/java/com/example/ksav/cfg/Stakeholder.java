package com.example.ksav.cfg;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Stakeholder extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_stakeholder);
    }
    public void toEducation(View view){
        Intent toEducation = new Intent(this,Education.class);
        startActivity(toEducation);
    }
}
