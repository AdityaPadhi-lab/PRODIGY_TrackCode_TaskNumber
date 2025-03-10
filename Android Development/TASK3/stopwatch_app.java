package com.example.stopwatch;

import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private TextView timerText;
    private Button startButton, pauseButton, resetButton;
    private Handler handler = new Handler();
    private long startTime = 0L, timeInMillis = 0L, updatedTime = 0L, timeSwapBuff = 0L;
    private boolean isRunning = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        timerText = findViewById(R.id.timerText);
        startButton = findViewById(R.id.startButton);
        pauseButton = findViewById(R.id.pauseButton);
        resetButton = findViewById(R.id.resetButton);

        startButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!isRunning) {
                    startTime = System.currentTimeMillis() - timeSwapBuff;
                    handler.postDelayed(updateTimer, 0);
                    isRunning = true;
                }
            }
        });

        pauseButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isRunning) {
                    timeSwapBuff = timeInMillis;
                    handler.removeCallbacks(updateTimer);
                    isRunning = false;
                }
            }
        });

        resetButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                timeSwapBuff = 0L;
                timeInMillis = 0L;
                updatedTime = 0L;
                timerText.setText("00:00:000");
                handler.removeCallbacks(updateTimer);
                isRunning = false;
            }
        });
    }

    private Runnable updateTimer = new Runnable() {
        public void run() {
            timeInMillis = System.currentTimeMillis() - startTime;
            updatedTime = timeSwapBuff + timeInMillis;
            int secs = (int) (updatedTime / 1000);
            int mins = secs / 60;
            secs = secs % 60;
            int millis = (int) (updatedTime % 1000);
            timerText.setText(String.format("%02d:%02d:%03d", mins, secs, millis));
            handler.postDelayed(this, 10);
        }
    };
}
