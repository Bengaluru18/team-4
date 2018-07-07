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

public class Education extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_education);

    }
    public void toMainActivity(View view){
        json();
        Toast.makeText(this,"Form submitted successfully",Toast.LENGTH_SHORT).show();
        Intent toMainActivity = new Intent(this,MainActivity.class);
        startActivity(toMainActivity);
    }

    public void json(){
        JSONObject obj = new JSONObject();
        try {
            obj.put("comment",((EditText)findViewById(R.id.editText)).getText().toString());
            /*e learning*/
            int resRg;
            RadioGroup rg1 = (RadioGroup) findViewById(R.id.radio1);
            final String value1 =
                    ((RadioButton)findViewById(rg1.getCheckedRadioButtonId()))
                            .getText().toString();
            if(value1.equals("Yes"))
                resRg= 1;
            else
                resRg = 0;
            obj.put("e learning",resRg);


            RadioGroup rg2 = (RadioGroup) findViewById(R.id.radio2);
            final String value2 =
                    ((RadioButton)findViewById(rg2.getCheckedRadioButtonId()))
                            .getText().toString();
            if(value1.equals("Yes"))
                resRg= 1;
            else
                resRg = 0;
            obj.put("medium of instruction",resRg);

            obj.put("CLUSTER",((EditText)findViewById(R.id.clusterEditText)).getText().toString());
            obj.put("TEACHERS",Integer.parseInt(((EditText)findViewById(R.id.teachersEditText)).getText().toString()));
            obj.put("UNDERSTANDING",Integer.parseInt(((EditText)findViewById(R.id.understandingEditText)).getText().toString()));
            obj.put("TEACHERS_QUALITY",Integer.parseInt(((EditText)findViewById(R.id.teachersQualityEditText)).getText().toString()));
            obj.put("NO_OF_MALE_TEACHERS",Integer.parseInt(((EditText)findViewById(R.id.boysEditText)).getText().toString()));
            obj.put("NO_OF_FEMALE_TEACHERS",Integer.parseInt(((EditText)findViewById(R.id.FemaleEditText)).getText().toString()));
            obj.put("NO_OF_PRIMARY_SCHOOL_CHILDREN",Integer.parseInt(((EditText)findViewById(R.id.primarySchoolEditText)).getText().toString()));
            obj.put("NO_OF_SECONDARY_SCHOOL_CHILDREN",Integer.parseInt(((EditText)findViewById(R.id.secondarySchoolEditText)).getText().toString()));

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
