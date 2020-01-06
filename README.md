# hass-bardolph
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

HASS custom component to load Bardolph (simple scripting utility for LIFX light bulbs by Al Fontes, Jr.) The **lsrun** and **lscap** command-line tools are implented as HASS services.
Please familiarize yourself with **[Bardolph](https://bardolph.org)** before installing this integration.

# Installation instructions

- In HACS Settings, add "JAAlperin/hass-bardolph" as an "Integration" Custom Repository.  Then install it.
- In lieu of HACS, copy the contents of `custom_components/bardolph/` to `<your config dir>/custom_components/bardolph/`.
- Add the following to your `configuration.yaml`:

```yaml
bardolph:
```
- Restart Home Assistant

# Usage

See the Home Assistant description of [Service Calls](https://www.home-assistant.io/docs/scripts/service-calls/)

![lsrun](https://github.com/JAAlperin/hass-bardolph/blob/master/screenshots/lsrun.jpg)

![lscap](https://github.com/JAAlperin/hass-bardolph/blob/master/screenshots/lscap.jpg)
