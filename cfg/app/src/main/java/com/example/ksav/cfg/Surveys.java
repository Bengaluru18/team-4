package com.example.ksav.cfg;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

public class Surveys extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_surveys);
    }
    public void nextFacilities(View view){
        json();
        Intent toFacilities = new Intent(this,Facilities.class);
        startActivity(toFacilities);
    }
    public void json(){
        JSONObject obj = new JSONObject();
        try {
            obj.put("comment",((EditText)findViewById(R.id.editText)).getText().toString());

            obj.put("No.of Active Projecdts",((EditText)findViewById(R.id.activeProjectsEditText)).getText().toString());
            obj.put("status",((EditText)findViewById(R.id.statusEditText)).getText().toString());
            obj.put("No.of Months completed after the project",Integer.parseInt(((EditText)findViewById(R.id.monthsEditText)).getText().toString()));
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
