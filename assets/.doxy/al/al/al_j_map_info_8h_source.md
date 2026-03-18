

# File alJMapInfo.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Util**](dir_159863c77a352c26f2f5de8c6cd02385.md) **>** [**alJMapInfo.h**](al_j_map_info_8h.md)

[Go to the documentation of this file](al_j_map_info_8h.md)


```C++
#pragma once

struct JMapItem
{
        enum Type
        {
                Long,
                String,
                Float,
                Long2,
                Short,
                Byte,
                StringPtr,
                Null
        };

        u32  mHash;
        u32  mMask;
        u16  mDataOffset;
        u8   mShift;
        Type mType;
};

struct JMapData
{
        int _0;
        int mNumData;
        int mDataOffset;
        int _C;

        const JMapItem* getItems()
        {
                return reinterpret_cast<const JMapItem*>( reinterpret_cast<const u8*>( this ) +
                                                          sizeof( JMapData ) );
        }

        const JMapItem* getItem( s32 index )
        {
                return &getItems()[ index ];
        }

        static const JMapData* fromData( const void* data )
        {
                return static_cast<const JMapData*>( data );
        }
};

class JMapInfo
{
private:
        const JMapData* mData;
        const char*     mName;

public:
        bool attach( const void* data );

        int  searchItemInfo( const char* );
        bool getValueFast( int, int index, u64* out );

public:
        JMapInfo();
};
```


