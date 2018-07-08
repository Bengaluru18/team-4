package com.example.ksav.cfg;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.VolleyLog;
import com.android.volley.toolbox.HttpHeaderParser;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void nextButton(View view){
        json();
        Intent toHealthIntent = new Intent(this,HealthActivity.class);
        startActivity(toHealthIntent);
    }

    public void json(){
        final Map<String,String> obj = new HashMap();


            obj.put("comment",((EditText)findViewById(R.id.editText)).getText().toString());
            obj.put("Locality",((EditText)findViewById(R.id.localityEditText)).getText().toString());
            obj.put("SchoolID",((EditText)findViewById(R.id.idEditText)).getText().toString());
            obj.put("S_name",((EditText)findViewById(R.id.nameEditText)).getText().toString());
            obj.put("NGO_No",((EditText)findViewById(R.id.noOfNgoEditText)).getText().toString());
            obj.put("S_No",((EditText)findViewById(R.id.schoolStrengthEditText)).getText().toString());
            obj.put("G_No",((EditText)findViewById(R.id.girlsEditText)).getText().toString());
            obj.put("B_No",((EditText)findViewById(R.id.boysEditText)).getText().toString());
            obj.put("Amount",((EditText)findViewById(R.id.amountEditText)).getText().toString());
            obj.put("District",((EditText)findViewById(R.id.clusterEditText)).getText().toString());
            obj.put("block",((EditText)findViewById(R.id.blockEditText)).getText().toString());
            obj.put("region",((EditText)findViewById(R.id.regionEditText)).getText().toString());
            obj.put("State",((EditText)findViewById(R.id.stateEditText)).getText().toString());



        Toast.makeText(this,String.valueOf(obj),Toast.LENGTH_LONG).show();





            RequestQueue requestQueue = Volley.newRequestQueue(this);
            String URL = "http://13.229.96.198:5000/insertworker";
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
