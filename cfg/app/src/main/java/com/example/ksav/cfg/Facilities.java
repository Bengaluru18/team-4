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

public class Facilities extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_facilities);
    }

    public void toStakeHolder(View view){
        json();
        Intent toFacilities = new Intent(this,Stakeholder.class);
        startActivity(toFacilities);
    }

    public void json(){
        JSONObject obj = new JSONObject();
        try {

            obj.put("comment",((EditText)findViewById(R.id.editText)).getText().toString());

            int resRg;
            RadioGroup rg1 = (RadioGroup) findViewById(R.id.radio1);
            final String value1 =
                    ((RadioButton)findViewById(rg1.getCheckedRadioButtonId()))
                            .getText().toString();
            if(value1.equals("Yes"))
                resRg= 1;
            else
                resRg = 0;
            obj.put("midday meals",resRg);

            obj.put("SPORTS",Integer.parseInt(((EditText)findViewById(R.id.sportsEditText)).getText().toString()));
            obj.put("CONSTRUCTION",Integer.parseInt(((EditText)findViewById(R.id.constructionEditText)).getText().toString()));
            obj.put("BAGS_NOTEBOOKS",Integer.parseInt(((EditText)findViewById(R.id.bagsNotebooksEditText)).getText().toString()));
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
