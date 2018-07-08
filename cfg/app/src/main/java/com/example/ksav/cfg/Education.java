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
        final Map<String,String> obj = new HashMap();

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
            obj.put("e learning",String.valueOf(resRg));


        obj.put("Med_ist",((EditText)findViewById(R.id.medist)).getText().toString());


//            obj.put("CLUSTER",((EditText)findViewById(R.id.clusterEditText)).getText().toString());
        int id=22;
        obj.put("ID",String.valueOf(id++));

        obj.put("T_No",((EditText)findViewById(R.id.teachersEditText)).getText().toString());
            obj.put("Stud_Un",((EditText)findViewById(R.id.understandingEditText)).getText().toString());
            obj.put("Teach_qual",((EditText)findViewById(R.id.teachersQualityEditText)).getText().toString());
            obj.put("MT_No",((EditText)findViewById(R.id.maleEditText)).getText().toString());
            obj.put("FT_No",((EditText)findViewById(R.id.FemaleEditText)).getText().toString());
            obj.put("P_stud",((EditText)findViewById(R.id.primarySchoolEditText)).getText().toString());
            obj.put("S_stud",((EditText)findViewById(R.id.secondarySchoolEditText)).getText().toString());
        obj.put("Comment",((EditText)findViewById(R.id.editText)).getText().toString());





        Toast.makeText(this,String.valueOf(obj),Toast.LENGTH_LONG).show();

        RequestQueue requestQueue = Volley.newRequestQueue(this);
        String URL = "http://13.229.96.198:5000/insertEducation";
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
