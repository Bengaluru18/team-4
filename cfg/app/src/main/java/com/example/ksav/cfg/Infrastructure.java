package com.example.ksav.cfg;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class Infrastructure extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_infrastructure);
    }
    public void nextAcademics(View view){
        json();
        Intent toAcademics = new Intent(this,Academics.class);
        startActivity(toAcademics);
    }
    public void json(){
        final Map<String,String> obj = new HashMap();
        int id = 11;
        obj.put("ID",String.valueOf(id++));

            obj.put("Comment",((EditText)findViewById(R.id.editText)).getText().toString());

            obj.put("C_No",((EditText)findViewById(R.id.classRoomsEditText)).getText().toString());
            obj.put("B_No",((EditText)findViewById(R.id.blackBoardsEditText)).getText().toString());
            obj.put("Ben_No",((EditText)findViewById(R.id.benchesChairsEditText)).getText().toString());
            int resRg;
            RadioGroup rg1 = (RadioGroup) findViewById(R.id.radio1);
            final String value1 =
                    ((RadioButton)findViewById(rg1.getCheckedRadioButtonId()))
                            .getText().toString();
            if(value1.equals("Yes"))
                resRg= 1;
            else
                resRg = 0;
            obj.put("Lib",String.valueOf(resRg));


            RadioGroup rg2 = (RadioGroup) findViewById(R.id.radio2);
            final String value2 =
                    ((RadioButton)findViewById(rg2.getCheckedRadioButtonId()))
                            .getText().toString();
            if(value2.equals("Yes"))
                resRg= 1;
            else
                resRg = 0;
            obj.put("Lab",String.valueOf(resRg));

            obj.put("Lab_Lib",((EditText)findViewById(R.id.labsQualityEditText)).getText().toString());

            RadioGroup rg3 = (RadioGroup) findViewById(R.id.radio3);
            final String value3 =
                    ((RadioButton)findViewById(rg3.getCheckedRadioButtonId()))
                            .getText().toString();
            if(value3.equals("Yes"))
                resRg= 1;
            else
                resRg = 0;
            obj.put("Comp",String.valueOf(resRg));


            obj.put("Com_No",((EditText)findViewById(R.id.noOfComputersEditText)).getText().toString());

            obj.put("Toil_Q",((EditText)findViewById(R.id.toiletsQualityEditText)).getText().toString());


            RadioGroup rg4 = (RadioGroup) findViewById(R.id.radio4);
            final String value4 =
                    ((RadioButton)findViewById(rg4.getCheckedRadioButtonId()))
                            .getText().toString();
            if(value4.equals("Yes"))
                resRg= 1;
            else
                resRg = 0;
            obj.put("Toil_Co",String.valueOf(resRg));


            obj.put("Build",((EditText)findViewById(R.id.stabilityOfBuildingEditText)).getText().toString());


        Toast.makeText(this,String.valueOf(obj),Toast.LENGTH_LONG).show();




        RequestQueue requestQueue = Volley.newRequestQueue(this);
        String URL = "http://13.229.96.198:5000/insertinfra";
//        String URL = "https://reqres.in/api/users";

//            final String requestBody = obj.toString();
        Toast.makeText(this,"1",Toast.LENGTH_SHORT).show();
        StringRequest stringRequest = new StringRequest(Request.Method.POST, URL, new Response.Listener<String>() {

            @Override
            public void onResponse(String response) {

                Log.i("VOLLEY", response);
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.e("VOLLEY", error.toString());
            }
        }) {
            @Override
            protected Map<String, String> getParams() throws AuthFailureError {
                Map<String,String> m = new HashMap<>();
                m.put("name","some name");
                m.put("job","some job");
                return obj;
            }
        };
        Toast.makeText(this,"3",Toast.LENGTH_SHORT).show();
        requestQueue.add(stringRequest);
    }












}
