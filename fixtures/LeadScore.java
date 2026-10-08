package org.example.hermeslab;
public final class LeadScore {
  public static int classify(int purchases, boolean highInterest) {
    if (purchases >= 3) return 100;
    if (highInterest) return 50;
    return 10;
  }
}
