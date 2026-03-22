

# File alSystemKit.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**System**](dir_e87416df8bf4bca963edaeb94e5411bb.md) **>** [**alSystemKit.cpp**](al_system_kit_8cpp.md)

[Go to the documentation of this file](al_system_kit_8cpp.md)


```C++
#include <File/alFileLoader.h>
#include <Save/alSaveDataDirector.h>
#include <System/Application.h>
#include <System/alSystemKit.h>

namespace al
{

void SystemKit::createFileLoader( int r1 )
{
        mFileLoader = new FileLoader( r1 );
}

void SystemKit::createSaveDataSystem( u32 r1, s32 r2 )
{
        mSaveDataDirector = new SaveDataDirector( r1, r2 );
}

} // namespace al

namespace alProjectInterface
{

al::SystemKit* getSystemKit()
{
        return al::getApplication()->getSystemKit();
}

} // namespace alProjectInterface
```


