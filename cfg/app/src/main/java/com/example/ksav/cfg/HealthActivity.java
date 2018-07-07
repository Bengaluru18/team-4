package com.example.ksav.cfg;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

public class HealthActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_health);
    }
    public void nextHealth(View view){
        json();
        Intent toInfrastructure = new Intent(this,Infrastructure.class);
        startActivity(toInfrastructure);
    }
    public void json(){
        JSONObject obj = new JSONObject();
        try {

            obj.put("comment",((EditText)findViewById(R.id.editText)).getText().toString());

            obj.put("NO_OF_PROG",Integer.parseInt(((EditText)findViewById(R.id.healthProgramsEditText)).getText().toString()));
            obj.put("FIRST_AID",Integer.parseInt(((EditText)findViewById(R.id.firstAidKitsEditText)).getText().toString()));
            int resRg;
            RadioGroup rg1 = (RadioGroup) findViewById(R.id.radio1);
            final String value1 =
                    ((RadioButton)findViewById(rg1.getCheckedRadioButtonId()))
                            .getText().toString();
            if(value1.equals("Yes"))
                resRg= 1;
            else
                resRg = 0;
            obj.put("medicine distributed by dopi",resRg);


            RadioGroup rg2 = (RadioGroup) findViewById(R.id.radio2);
            final String value2 =
                    ((RadioButton)findViewById(rg2.getCheckedRadioButtonId()))
                            .getText().toString();
            if(value2.equals("Yes"))
                resRg= 1;
            else
                resRg = 0;
            obj.put("school mental health",resRg);


            RadioGroup rg3 = (RadioGroup) findViewById(R.id.radio3);
            final String value3 =
                    ((RadioButton)findViewById(rg3.getCheckedRadioButtonId()))
                            .getText().toString();
            if(value3.equals("Yes"))
                resRg= 1;
            else
                resRg = 0;
            obj.put("training on hygiene",resRg);
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
