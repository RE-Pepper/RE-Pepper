

# File alKCollisionServer.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Collision**](dir_b09a96783c41b30bc153ca6a88ba8512.md) **>** [**alKCollisionServer.cpp**](al_k_collision_server_8cpp.md)

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


