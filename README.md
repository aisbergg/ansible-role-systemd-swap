# Ansible Role: `aisbergg.systemd-swap`

This Ansible role installs and configures the [`systemd-swap`](https://github.com/aurora/systemd-swap) script on Linux systems, which can be used to create ZRAM and ZSWAP devices.

You can use `swapon -s` to list currently present SWAP devices.

## Requirements

None.

## Role Variables

| Variable | Default | Comments |
|----------|---------|----------|
| `systemd_swap_service_enabled` | `true` | Enable the systemd-swap service. |
| `systemd_swap_service_state` | `started` | Set the run state of the systemd-service. |
| `systemd_swap_zram_enabled` | `false` | Enable ZRAM. |
| `systemd_swap_zram_size` | `25%` | Amount of RAM to dedicate to ZRAM. If no unit is specified it will default to 'M'. A percent value '%' refers to the amount of total available memory. The following units are allowed: K,M,G,T,P,E,Z,Y,KiB,KB,MiB,...  |
| `systemd_swap_zram_streams` | `{{ ansible_processor_cores }}` | Number of processor cores to use for compression. |
| `systemd_swap_zram_alg` | `lzo` | Compression algorithm to use for ZRAM. Use `zramctl -h` to get a list of valid compression algorithms to use. |
| `systemd_swap_zram_prio` | `32767` | Usage priority of the ZRAM devices. |
| `systemd_swap_zswap_enabled` | `false` | Enable ZSWAP. |
| `systemd_swap_zswap_compressor` | `lzo` | Compression algorithm to use for ZRAM. |
| `systemd_swap_zswap_max_pool_percent` | `25` | Max pool size. |
| `systemd_swap_zswap_zpool` | `zbud` | Type of ZSWAP pool. |
| `systemd_swap_swapfc_enabled` | `false` | Enable chunked swap files. |
| `systemd_swap_swapfc_force_use_loop` | `false` | Force usage of swapfile + loop. |
| `systemd_swap_swapfc_frequency` | `1s` | How often check free swap space. |
| `systemd_swap_swapfc_chunk_size` | `512M` | Size of a chunk. |
| `systemd_swap_swapfc_max_count` | `8` | Number of chunks to allocate. |
| `systemd_swap_swapfc_free_swap_perc` | `15` | Add a new chunk, if threshold is reached (if free space < 15%). |
| `systemd_swap_swapfc_nocow` | `true` | Disable CoW on swapfile. |
| `systemd_swap_swapfc_directio` | `true` | Use directio for loop dev. |
| `systemd_swap_swapfc_force_preallocated` | `false` | Preallocate created files. |
| `systemd_swap_swapd_auto_swapon` | `true` | Find and auto swapon all available swap devices |
| `systemd_swap_swapd_prio` | `1024` | Priority of systemd services. |

## Example Playbook

```yaml
- hosts: all
  vars:
    systemd_swap_service_enabled: true
    systemd_swap_zram_enabled: true
    systemd_swap_zram_size: 25%
    systemd_swap_zram_prio: 32767
  roles:
    - aisbergg.systemd-swap
```

## Dependencies

None.

## License

MIT

## Author Information

Andre Lehmann (aisberg@posteo.de)
