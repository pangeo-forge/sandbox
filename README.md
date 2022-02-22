# sandbox: `binder` branch

This branch exists to build Docker images for the the Pangeo Forge Sandbox as well as provide a Dockerfile for the Sandbox's Binder environment.

To build images, edit the contents of `/image` then run

```
docker build -t pangeo/pangeo-forge-sandbox:$TAG -f ./image/Dockerfile ./image --platform linux/amd64
```

where `TAG` is a composite of a Pangeo Notebook version and a `pangeo-forge-recipes` version.

Users with Pangeo Docker Hub credentials can push built images with

```
docker push pangeo/pangeo-forge-sandbox:$TAG
```

The `/binder/Dockerfile`, used to build the Sandbox's Binder environment, simply pulls `pangeo/pangeo-forge-sandbox:$TAG` from Docker Hub. (These images could also be built at runtime, but hopefully pushing them to Docker Hub saves user start up time.)
