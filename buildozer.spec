[app]
title = Control Remoto
package.name = remotecontrol
package.domain = org.myapp
source.dir = .
source.include_exts = py
version = 1.0.0
requirements = python3,flet>=0.15.0,kivymd

android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a
android.api = 31
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1
