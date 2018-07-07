package com.example.ksav.cfg;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

public class Stakeholder extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_stakeholder);
    }
    public void toEducation(View view){
        json();
        Intent toEducation = new Intent(this,Education.class);
        startActivity(toEducation);
    }
    public void json(){
        JSONObject obj = new JSONObject();
        try {
            obj.put("Teachers training",Integer.parseInt(((EditText)findViewById(R.id.teachersEditText)).getText().toString()));
            obj.put("parents meeting",Integer.parseInt(((EditText)findViewById(R.id.parentsEditText)).getText().toString()));
            obj.put("Alumni associaition",Integer.parseInt(((EditText)findViewById(R.id.AlumniEditText)).getText().toString()));
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
