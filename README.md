# hass-bardolph
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

HASS custom component to load Bardolph (simple scripting utility for LIFX light bulbs by Al Fontes, Jr.) The **lsrun** and **lscap** command-line tools are implented as HASS services.
Please familiarize yourself with **[Bardolph](https://bardolph.org)** before installing this integration.

# Installation instructions

- Copy the contents of `custom_components/bardolph/` to `<your config dir>/custom_components/bardolph/`.
- Add the following to your `configuration.yaml`:

```yaml
bardolph:
```
- Restart Home Assistant

# Usage

See the Home Assistant description of [Service Calls](https://www.home-assistant.io/docs/scripts/service-calls/)
