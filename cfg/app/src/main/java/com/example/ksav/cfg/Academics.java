


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
        final Map<String,String> obj = new HashMap();
        int id=11;
        obj.put("S_ID",String.valueOf(id++));
        obj.put("No_Aprogs",((EditText)findViewById(R.id.AcademicsEditText)).getText().toString());
        obj.put("Passper",((EditText)findViewById(R.id.passPercentageEditText)).getText().toString());
        obj.put("Comments",((EditText)findViewById(R.id.editText)).getText().toString());


        Toast.makeText(this,String.valueOf(obj),Toast.LENGTH_LONG).show();

        RequestQueue requestQueue = Volley.newRequestQueue(this);
        String URL = "http://13.229.96.198:5000/insertacademics";
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
