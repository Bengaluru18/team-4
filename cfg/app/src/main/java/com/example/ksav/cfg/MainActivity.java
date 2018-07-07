package com.example.ksav.cfg;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void nextButton(View view){
        json();
        Intent toHealthIntent = new Intent(this,HealthActivity.class);
        startActivity(toHealthIntent);
    }

    public void json(){
        JSONObject obj = new JSONObject();
        try {
            obj.put("ID",((EditText)findViewById(R.id.idEditText)).getText().toString());
            obj.put("NAME",((EditText)findViewById(R.id.nameEditText)).getText().toString());
            obj.put("EXISTINGPROG",Integer.parseInt(((EditText)findViewById(R.id.noOfNgoEditText)).getText().toString()));
            obj.put("Strength",Integer.parseInt(((EditText)findViewById(R.id.schoolStrengthEditText)).getText().toString()));
            obj.put("NO_OF_GIRLS",Integer.parseInt(((EditText)findViewById(R.id.girlsEditText)).getText().toString()));
            obj.put("NO_OF_BOYS",Integer.parseInt(((EditText)findViewById(R.id.boysEditText)).getText().toString()));
            obj.put("FUNDS",Integer.parseInt(((EditText)findViewById(R.id.amountEditText)).getText().toString()));
            obj.put("CLUSTER",((EditText)findViewById(R.id.clusterEditText)).getText().toString());
            obj.put("BLOCK",((EditText)findViewById(R.id.blockEditText)).getText().toString());
            obj.put("REGION",((EditText)findViewById(R.id.regionEditText)).getText().toString());
            obj.put("STATE",((EditText)findViewById(R.id.stateEditText)).getText().toString());
        } catch (JSONException e) {
            e.printStackTrace();
        }

        Toast.makeText(this,String.valueOf(obj),Toast.LENGTH_LONG).show();

        /*
        try {
            URL url = new URL("/media/webservice/httppost.php");
            URLConnection conn = url.openConnection();
            conn.setDoOutput(true);
            OutputStreamWriter wr = new OutputStreamWriter(conn.getOutputStream());
            wr.write(String.valueOf(obj));
            wr.flush();
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    */

    }







}
