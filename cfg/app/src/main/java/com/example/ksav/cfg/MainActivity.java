package com.example.ksav.cfg;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void nextButton(View view){
        Intent toHealthIntent = new Intent(this,HealthActivity.class);
        startActivity(toHealthIntent);
    }


}

class jsonSend{
    public static void main(String[] args){
        JSONObject obj = new JSONObject();
        
    }
}