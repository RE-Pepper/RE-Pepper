

# File alByamlHashIter.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Yaml**](dir_a66705d5185d64e99b2223010bf5d935.md) **>** [**alByamlHashIter.cpp**](al_byaml_hash_iter_8cpp.md)

[Go to the documentation of this file](al_byaml_hash_iter_8cpp.md)


```C++
#include <Yaml/alByamlHashIter.h>

namespace al
{

const ByamlHashPair* ByamlHashIter::findPair( int keyIdx ) const
{
        const ByamlHashPair* table = getPairTable();
        int                  low   = 0;

        if ( mData )
        {
                int high = getSize();
                if ( high > 0 )
                {
                        const ByamlHashPair* pair;
                        int                  idx;
                        while ( true )
                        {
                                idx           = ( low + high ) / 2;
                                pair          = &table[ idx ];
                                const int res = keyIdx - ( pair->getKeyIndex() );
                                if ( res < 0 )
                                        high = idx;
                                if ( res > 0 )
                                        low = idx + 1;
                                if ( res == 0 )
                                        return &table[ idx ];
                                if ( high <= low )
                                        break;
                        }
                }
        }

        return nullptr;
}

} // namespace al
```


