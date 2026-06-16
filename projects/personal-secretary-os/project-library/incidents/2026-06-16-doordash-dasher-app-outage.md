# DoorDash / Dasher App Outage Evidence Note

## Кратко по-русски

16 июня 2026 около 10:24 AM ET у владельца возникли проблемы с DoorDash / Dasher App. По совокупности признаков это выглядело как массовый сбой DoorDash на стороне приложения/логина, а не как локальная проблема телефона или интернета.

Зафиксированные признаки:

- Dasher App показывал `Dash Paused`;
- кнопка `Resume dash` была нестабильной: то красная/активная, то серая/недоступная;
- DoorDash показывал ошибку входа: `Sorry, there was a problem logging you in. Please check your connection and try again.`;
- Downdetector показывал резкий всплеск жалоб, основное: App и Login;
- Reddit `r/doordash_drivers` показывал свежие сообщения водителей: людей одновременно разлогинило, у некоторых зависли drop-off, mark as delivered, фото подтверждения и завершение заказа.

Вывод: наиболее вероятно, это был DoorDash-side App/Login outage. Практическая рекомендация при таком сбое: не нажимать `End Dash`, не переустанавливать приложение во время login outage, сохранять скриншоты, фиксировать время, после восстановления проверить earnings и при необходимости писать в поддержку, чтобы сбой не повлиял на ratings, completion rate, acceptance rate или dash status.

---

Date: 2026-06-16
Approx. time observed: around 10:24 AM ET
Project/context: personal secretary intake; DoorDash/gig-work operational continuity
Type: incident evidence note
Lifecycle status: captured

## Summary

The owner experienced DoorDash / Dasher App problems during an apparent live outage. The issue looked like a platform-side DoorDash App/Login outage rather than a local phone or connection issue.

## User-Observed Symptoms

- Dasher App showed `Dash Paused`.
- Message: `You won't get offers while you're paused`.
- `Resume dash` button appeared intermittently available: sometimes red/active, sometimes gray/unavailable.
- DoorDash login screen showed: `Sorry, there was a problem logging you in. Please check your connection and try again.`

## External Evidence Captured In Conversation

### Downdetector screenshot

The owner provided a Downdetector screenshot showing:

- sharp vertical spike at `Now`;
- high volume of user reports;
- nationwide red report map;
- reported problem mix:
  - 73% App;
  - 24% Login;
  - 2% Website.

### Reddit screenshot

The owner provided a screenshot from `r/doordash_drivers` showing a recent post titled:

`Did anyone else just get logged out?`

Visible timing and engagement:

- `28 upvotes`;
- `78 comments`;
- comments visible from roughly 41 minutes to 8 minutes before screenshot capture.

Visible user comments reported:

- being logged out in the middle of drop-off;
- being logged out after marking an order delivered;
- app going down before taking the drop-off photo;
- inability to complete the order;
- concern about being paid;
- multiple users saying it was not just them.

## Assessment

The evidence strongly suggests a DoorDash-side App/Login outage, not a local device-only issue.

Independent supporting signals:

1. Dasher App stuck on paused / unstable resume.
2. DoorDash login failure.
3. Downdetector live spike with App/Login as dominant problem categories.
4. Reddit driver reports of simultaneous logout, incomplete drop-offs, and inability to complete orders.

## Practical Guidance Preserved

During this type of outage:

- do not press `End Dash` if preserving the dash slot matters;
- do not uninstall/reinstall immediately during login outage, because re-login may fail;
- take screenshots with phone time visible when possible;
- preserve screenshots of Dasher state, login error, Downdetector spike, and Reddit driver reports;
- if an active order is involved, preserve order details, restaurant, drop-off status, time, and any error messages;
- after recovery, verify earnings and order completion status;
- if contacting support, explicitly ask that ratings, completion rate, acceptance rate, and dash status not be harmed by a platform outage.

## Support Message Draft

```text
Hi, my DoorDash/Dasher app appears to be affected by the current outage. The app is stuck on Dash Paused, the Resume Dash button is unavailable or intermittent, and the DoorDash login screen is also showing: “Sorry, there was a problem logging you in. Please check your connection and try again.” Downdetector is showing a major spike in DoorDash reports right now, mostly App and Login problems. Other drivers are also reporting being logged out and unable to complete deliveries. Please make sure this does not affect my ratings, completion rate, acceptance rate, or dash status. I have screenshots with the time.
```

## Reuse Trigger

Load this note when the owner asks about:

- DoorDash / Dasher App outage;
- app stuck on pause;
- login error;
- `Resume dash` unavailable;
- incomplete delivery due to platform issue;
- protecting ratings or pay during a gig-app outage.

## Boundary

This note stores operational facts and evidence summary only. It does not store private account credentials, personal identifiers, customer information, or full screenshots.
