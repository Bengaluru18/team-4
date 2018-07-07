package com.example.ksav.cfg;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

public class Academics extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_academics);
    }

    public void nextSurveys(View view){
        json();
        Intent toSurveys = new Intent(this,Surveys.class);
        startActivity(toSurveys);
    }

    public void json(){
        JSONObject obj = new JSONObject();
        try {
            obj.put("NO_OF_ACADEMIC_PROGRAMS",Integer.parseInt(((EditText)findViewById(R.id.AcademicsEditText)).getText().toString()));
            obj.put("PASS_PERCENTAGE",Integer.parseInt(((EditText)findViewById(R.id.passPercentageEditText)).getText().toString()));
            obj.put("comment",((EditText)findViewById(R.id.editText)).getText().toString());

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
