rm -rf copy-dst
uw file copy --target-dir copy-dst --config-file copy-config.yaml config files
echo
tree copy-dst
