

# File alByamlHashIter.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Yaml**](dir_4db20b6947036956387e84dab645aa7e.md) **>** [**alByamlHashIter.h**](al_byaml_hash_iter_8h.md)

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


