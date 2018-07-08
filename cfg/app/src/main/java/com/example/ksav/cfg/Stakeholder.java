package com.example.ksav.cfg;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
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
        final Map<String,String> obj = new HashMap();
        int id = 21;
        obj.put("ID",String.valueOf(id++));

            obj.put("T_Train",((EditText)findViewById(R.id.teachersEditText)).getText().toString());
            obj.put("P_Meet",((EditText)findViewById(R.id.parentsEditText)).getText().toString());
            obj.put("Alum",((EditText)findViewById(R.id.AlumniEditText)).getText().toString());
            obj.put("Comments",((EditText)findViewById(R.id.editText)).getText().toString());
        obj.put("SDCInv",((EditText)findViewById(R.id.sdmcEditText)).getText().toString());

        Toast.makeText(this,String.valueOf(obj),Toast.LENGTH_LONG).show();


        RequestQueue requestQueue = Volley.newRequestQueue(this);
        String URL = "http://13.229.96.198:5000/insertstake";
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
