# Reference: dhd/droid-hal-device.inc

%define vendor xiaomi
%define device polaris

%define vendor_pretty Xiaomi
%define device_pretty Mix 2s

%define droid_target_aarch64 1
%define enable_kernel_update 1

%define android_config \
  #define WANT_ADRENO_QUIRKS 1 \
%{nil}

# Don't create systemd mount units for these
%define makefstab_skip_entries /dev/cpuctl /dev/stune /sys/fs/pstore /mnt/vendor/persist

%include rpm/dhd/droid-hal-device.inc
