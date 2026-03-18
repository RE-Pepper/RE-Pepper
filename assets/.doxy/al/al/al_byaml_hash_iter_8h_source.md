

# File alByamlHashIter.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Yaml**](dir_ead735227c22214cb122acbd07613fdc.md) **>** [**alByamlHashIter.h**](al_byaml_hash_iter_8h.md)

[Go to the documentation of this file](al_byaml_hash_iter_8h.md)


```C++
#pragma once

#include <Yaml/alByamlData.h>

namespace al
{

class ByamlHashPair
{
private:
        union
        {
                ByamlDataType mType;
                u32           mKeyIndex;
        };

        u32 mValue;

public:
        ByamlDataType getType() const
        {
                return mType;
        }

        u32 getKeyIndex() const
        {
                return mKeyIndex & 0xFFFFFF;
        }

        u32 getValue() const
        {
                return mValue;
        }
};

class ByamlHashIter
{
private:
        struct Header
        {
                al::ByamlDataType type : 8;
                u32               hashAmount : 24;
        };

        union
        {
                const u8*     mData;
                uintptr_t     mDataPtr;
                const Header* mHeader;
        };

        const ByamlHashPair* getPairTable() const
        {
                return !mDataPtr ? nullptr : reinterpret_cast<ByamlHashPair*>( mDataPtr + sizeof( mDataPtr ) );
        }

        u32 getSize() const
        {
                return mHeader->hashAmount;
        }

public:
        ByamlHashIter( const u8* data ) : mData( data )
        {
        }

        const ByamlHashPair* findPair( int keyIdx ) const;
        bool                 getDataByKey( ByamlData* out, int index ) const;
};

} // namespace al
```


