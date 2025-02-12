# Change Log

## 3.0.0 (2022-05-11)

A major update that adds a parameter when you create a payment order

-   `create_payment_order` now also requires `SEK` or `NOK` as a parameter.
-   `se_organisation_number` changed format from `555555-5555` to `5555555555`.

## 2.1.0 (2022-04-26)

A minor update that prevents unintentional fast-forwarding through the stages close, split settle of a payment order.

-   Split and Settle a payment order now takes in an optional `fast_forward` parameter.

## 2.0.0 (2022-04-22)

A major update that adds two new endpoints to the SDK.

-   Payout endpoints are now implemented. You are now able to list payouts.

-   Ping endpoint is now implemented. You are now able to ping the API.

## 1.1.0-alpha (2022-04-01)

An SDK update to support new API changes regarding the date format of a payment order.

-   Dates are now returned in ISO 8601 format

-   Using `from_date` and `to_date` when getting payment orders also requires to be written in ISO 8601 format.

-   A Swish payment is now a m/e-commerce instead of mobile

## 1.0.0-alpha (2022-03-25)

-   The SDK have been updated to support all endpoints of payments API.

-   update_payment_order() now working.

-   Requirements for which python versions are compatible with the SDKt have been updated and checked.

    -   The SDK is compatible Python 3 versions 3.7 and later.

-   Tests to ensure that the SDK works on several operating systems have been implemented.
    -   The tests include: Ubuntu, Windows and Mac OS.

## 0.3.0 (2022-03-21)

An SDK update to support new API changes regarding the initialization of a payment.

-   Added `payment_iq` as a new provider when initiating a payment

## 0.2.0 (2022-03-21)

An SDK update to support new API changes regarding initialization of a payment.

-   Each order item now requires a merchant id
-   Unit-Tests updated to support this change
-   Documentation updated to support this change

## 0.1.0 (2022-03-14)

-   The SDK have been updated to support the whole payments API.
