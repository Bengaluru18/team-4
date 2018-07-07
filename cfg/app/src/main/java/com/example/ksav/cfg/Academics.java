package com.example.ksav.cfg;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Academics extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_academics);
    }

    public void nextSurveys(View view){
        Intent toSurveys = new Intent(this,Surveys.class);
        startActivity(toSurveys);
    }
}
