package com.example.qrcodescanner;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;
import com.google.mlkit.vision.barcode.Barcode;
import com.google.mlkit.vision.barcode.BarcodeScanner;
import com.google.mlkit.vision.barcode.BarcodeScanning;
import com.google.mlkit.vision.common.InputImage;
import java.io.IOException;

public class MainActivity extends AppCompatActivity {

    private TextView resultText;
    private ActivityResultLauncher<Intent> barcodeScannerLauncher;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        resultText = findViewById(R.id.resultText);
        Button scanButton = findViewById(R.id.scanButton);

        barcodeScannerLauncher = registerForActivityResult(
                new ActivityResultContracts.StartActivityForResult(),
                result -> {
                    if (result.getResultCode() == RESULT_OK && result.getData() != null) {
                        processBarcode(result.getData());
                    }
                }
        );

        scanButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Intent.ACTION_PICK);
                intent.setType("image/*");
                barcodeScannerLauncher.launch(intent);
            }
        });
    }

    private void processBarcode(Intent data) {
        try {
            InputImage image = InputImage.fromFilePath(this, data.getData());
            BarcodeScanner scanner = BarcodeScanning.getClient();
            scanner.process(image).addOnSuccessListener(barcodes -> {
                for (Barcode barcode : barcodes) {
                    String value = barcode.getRawValue();
                    resultText.setText(value);
                    if (barcode.getValueType() == Barcode.TYPE_URL) {
                        openLink(value);
                    }
                }
            }).addOnFailureListener(e -> resultText.setText("Scan failed!"));
        } catch (IOException e) {
            resultText.setText("Error loading image!");
        }
    }

    private void openLink(String url) {
        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
        startActivity(intent);
    }
}
