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

public class Infrastructure extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_infrastructure);
    }
    public void nextAcademics(View view){
        Intent toAcademics = new Intent(this,Academics.class);
        startActivity(toAcademics);
    }
    public void json(){
        JSONObject obj = new JSONObject();
        try {

            obj.put("comment",((EditText)findViewById(R.id.editText)).getText().toString());

            obj.put("No of class rooms",Integer.parseInt(((EditText)findViewById(R.id.classRoomsEditText)).getText().toString()));
            obj.put("No.of black boads",Integer.parseInt(((EditText)findViewById(R.id.blackBoardsEditText)).getText().toString()));
            obj.put("NO of benches and chairs",Integer.parseInt(((EditText)findViewById(R.id.benchesChairsEditText)).getText().toString()));
            int resRg;
            RadioGroup rg1 = (RadioGroup) findViewById(R.id.radio1);
            final String value1 =
                    ((RadioButton)findViewById(rg1.getCheckedRadioButtonId()))
                            .getText().toString();
            if(value1.equals("Yes"))
                resRg= 1;
            else
                resRg = 0;
            obj.put("library",resRg);


            RadioGroup rg2 = (RadioGroup) findViewById(R.id.radio2);
            final String value2 =
                    ((RadioButton)findViewById(rg2.getCheckedRadioButtonId()))
                            .getText().toString();
            if(value2.equals("Yes"))
                resRg= 1;
            else
                resRg = 0;
            obj.put("labs",resRg);

            obj.put("Labs and lib quality",Integer.parseInt(((EditText)findViewById(R.id.labsQualityEditText)).getText().toString()));

            RadioGroup rg3 = (RadioGroup) findViewById(R.id.radio3);
            final String value3 =
                    ((RadioButton)findViewById(rg3.getCheckedRadioButtonId()))
                            .getText().toString();
            if(value3.equals("Yes"))
                resRg= 1;
            else
                resRg = 0;
            obj.put("computers",resRg);


            obj.put("No of computers",Integer.parseInt(((EditText)findViewById(R.id.noOfComputersEditText)).getText().toString()));

            obj.put("toiles quality",Integer.parseInt(((EditText)findViewById(R.id.toiletsQualityEditText)).getText().toString()));


            RadioGroup rg4 = (RadioGroup) findViewById(R.id.radio4);
            final String value4 =
                    ((RadioButton)findViewById(rg4.getCheckedRadioButtonId()))
                            .getText().toString();
            if(value4.equals("Yes"))
                resRg= 1;
            else
                resRg = 0;
            obj.put("computers",resRg);


            obj.put("stability of building",Integer.parseInt(((EditText)findViewById(R.id.stabilityOfBuildingEditText)).getText().toString()));

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
