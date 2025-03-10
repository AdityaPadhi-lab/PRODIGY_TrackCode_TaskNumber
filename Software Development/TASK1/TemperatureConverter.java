package com.example.temperatureconverter;

import java.util.Scanner;

public class TemperatureConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter temperature value: ");
        double temperature = scanner.nextDouble();
        
        System.out.print("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ");
        char unit = scanner.next().toUpperCase().charAt(0);
        
        switch (unit) {
            case 'C':
                convertFromCelsius(temperature);
                break;
            case 'F':
                convertFromFahrenheit(temperature);
                break;
            case 'K':
                convertFromKelvin(temperature);
                break;
            default:
                System.out.println("Invalid unit entered. Please enter C, F, or K.");
        }
    }
    
    private static void convertFromCelsius(double celsius) {
        double fahrenheit = (celsius * 9/5) + 32;
        double kelvin = celsius + 273.15;
        System.out.println("Fahrenheit: " + fahrenheit);
        System.out.println("Kelvin: " + kelvin);
    }
    
    private static void convertFromFahrenheit(double fahrenheit) {
        double celsius = (fahrenheit - 32) * 5/9;
        double kelvin = celsius + 273.15;
        System.out.println("Celsius: " + celsius);
        System.out.println("Kelvin: " + kelvin);
    }
    
    private static void convertFromKelvin(double kelvin) {
        double celsius = kelvin - 273.15;
        double fahrenheit = (celsius * 9/5) + 32;
        System.out.println("Celsius: " + celsius);
        System.out.println("Fahrenheit: " + fahrenheit);
    }
}
