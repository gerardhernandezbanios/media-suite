$networkName = "media-suite-net"

if (!(docker network ls --format "{{.Name}}" | Select-String -Pattern $networkName)) {
    Write-Host "Creating network $networkName..."
    docker network create $networkName
} else {
    Write-Host "Network $networkName already exists."
}
