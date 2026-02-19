# This script creates a Docker network for the media suite containers.

# Note: You may need to run this script with elevated privileges (Run as Administrator) to set the execution policy.
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

$networkName = "media-suite-net"

if (!(docker network ls --format "{{.Name}}" | Select-String -Pattern $networkName)) {
    Write-Host "Creating network $networkName..."
    docker network create $networkName
} else {
    Write-Host "Network $networkName already exists."
}
