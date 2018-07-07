package com.example.ksav.cfg;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Surveys extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_surveys);
    }
    public void nextFacilities(View view){
        Intent toFacilities = new Intent(this,Facilities.class);
        startActivity(toFacilities);
    }
}
