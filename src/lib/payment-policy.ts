import { businessConfig } from "@/config/business";

export type ServicePaymentBreakdown = {
  initialPaymentCents: number;
  finalPaymentCents: number;
};

/** Apply the centrally configured service-payment policy to a fee expressed in ZAR cents. */
export function calculateServicePayment(feeCents: number): ServicePaymentBreakdown {
  if (!Number.isSafeInteger(feeCents) || feeCents < 0) {
    throw new RangeError("The engagement fee must be a non-negative amount in cents.");
  }

  if (feeCents < businessConfig.servicePaymentPolicy.thresholdCents) {
    return { initialPaymentCents: feeCents, finalPaymentCents: 0 };
  }

  const initialPaymentCents = Math.round(
    (feeCents * businessConfig.servicePaymentPolicy.depositPercent) / 100,
  );

  return {
    initialPaymentCents,
    finalPaymentCents: feeCents - initialPaymentCents,
  };
}