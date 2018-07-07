package example.javatpoint.com.seekbar;  
  
import android.support.v7.app.AppCompatActivity;  
import android.os.Bundle;  
import android.widget.SeekBar;  
import android.widget.Toast;  
  
public class MainActivity extends AppCompatActivity {  
    SeekBar seekBar;  
    @Override  
    protected void onCreate(Bundle savedInstanceState) {  
        super.onCreate(savedInstanceState);  
        setContentView(R.layout.activity_main);  
  
        seekBar=(SeekBar)findViewById(R.id.seekBar);  
        seekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {  
            @Override  
            public void onProgressChanged(SeekBar seekBar, int progress,  
                                          boolean fromUser) {  
                Toast.makeText(getApplicationContext(),"seekbar progress: "+progress, Toast.LENGTH_SHORT).show();  
            }  
  
            @Override  
            public void onStartTrackingTouch(SeekBar seekBar) {  
                Toast.makeText(getApplicationContext(),"seekbar touch started!", Toast.LENGTH_SHORT).show();  
            }  
  
            @Override  
            public void onStopTrackingTouch(SeekBar seekBar) {  
                Toast.makeText(getApplicationContext(),"seekbar touch stopped!", Toast.LENGTH_SHORT).show();  
            }  
        });  
    }  
}  