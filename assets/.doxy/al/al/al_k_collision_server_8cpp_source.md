

# File alKCollisionServer.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Collision**](dir_4625c3c25d458a4908e8cd58e73b9017.md) **>** [**alKCollisionServer.cpp**](al_k_collision_server_8cpp.md)

[Go to the documentation of this file](al_k_collision_server_8cpp.md)


```C++
#include <Collision/alKCollisionServer.h>
#include <Util/alJMapInfo.h>

namespace al
{

KCollisionServer::KCollisionServer() : mHeader( nullptr ), mAttributeInfo( new JMapInfo ), _8( 1.0 )
{
}

void KCollisionServer::setData( void* data )
{
        mHeaderData = data;

        if ( ( mHeader->verticesOffset & 0xffffff00 ) == 0 ) // ?
        {
                mHeader->verticesSection       = mHeaderDataBytes + mHeader->verticesOffset;
                mHeader->normalsSection        = mHeaderDataBytes + mHeader->normalsOffset;
                mHeader->trianglesSection      = mHeaderDataBytes + mHeader->trianglesOffset;
                mHeader->spatialIndicesSection = mHeaderDataBytes + mHeader->spatialIndicesOffset;
        }
}

void KCollisionServer::initKCollisionServer( void* kclData, const void* paData )
{
        setData( kclData );
        if ( paData )
                mAttributeInfo->attach( paData );
}

} // namespace al
```


