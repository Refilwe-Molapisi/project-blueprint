import { describe, expect, it } from "vitest";

import { calculateServicePayment } from "@/lib/payment-policy";

describe("service payment policy", () => {
  it("requires the full fee upfront for engagements below R2,000", () => {
    expect(calculateServicePayment(150_000)).toEqual({
      initialPaymentCents: 150_000,
      finalPaymentCents: 0,
    });
    expect(calculateServicePayment(199_900)).toEqual({
      initialPaymentCents: 199_900,
      finalPaymentCents: 0,
    });
  });

  it("splits engagements of R2,000 or more into an initial and final payment", () => {
    expect(calculateServicePayment(300_000)).toEqual({
      initialPaymentCents: 150_000,
      finalPaymentCents: 150_000,
    });
  });

  it("applies the 50/50 arrangement to exactly R2,000", () => {
    expect(calculateServicePayment(200_000)).toEqual({
      initialPaymentCents: 100_000,
      finalPaymentCents: 100_000,
    });
  });

  it("rejects negative or fractional-cent fees", () => {
    expect(() => calculateServicePayment(-1)).toThrow(RangeError);
    expect(() => calculateServicePayment(100.5)).toThrow(RangeError);
  });
});