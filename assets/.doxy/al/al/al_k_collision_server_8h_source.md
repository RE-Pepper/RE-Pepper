

# File alKCollisionServer.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Collision**](dir_b64277db147a0cb833174dd0bf4617cc.md) **>** [**alKCollisionServer.h**](al_k_collision_server_8h.md)

[Go to the documentation of this file](al_k_collision_server_8h.md)


```C++
#pragma once

class JMapInfo;

namespace al
{

struct KCollisionHeader
{
        union
        {
                u32   verticesOffset;
                void* verticesSection;
        };

        union
        {
                u32   normalsOffset;
                void* normalsSection;
        };

        union
        {
                u32   trianglesOffset;
                void* trianglesSection;
        };

        union
        {
                u32   spatialIndicesOffset;
                void* spatialIndicesSection;
        };

        static KCollisionHeader* fromData( void* data )
        {
                return static_cast<KCollisionHeader*>( data );
        }
};

class KCollisionServer
{
private:
        union
        {
                KCollisionHeader* mHeader;
                void*             mHeaderData;
                u8*               mHeaderDataBytes;
        };

        JMapInfo* mAttributeInfo;
        float     _8;

public:
        void setData( void* data );
        void initKCollisionServer( void* kclData, const void* paData );

public:
        KCollisionServer();
};

} // namespace al
```


