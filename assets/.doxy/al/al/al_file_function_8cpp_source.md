

# File alFileFunction.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**File**](dir_242a3082c7cfa68f514048551d44dd2a.md) **>** [**alFileFunction.cpp**](al_file_function_8cpp.md)

[Go to the documentation of this file](al_file_function_8cpp.md)


```C++
#include <File/alFileFunction.h>
#include <File/alFileLoader.h>
#include <Message/alMessageFunction.h>
#include <System/alSystemKit.h>
#include <Util/alStringUtil.h>

namespace al
{

void loadArchive( const sead::SafeString& archive )
{
        alProjectInterface::getSystemKit()->getFileLoader()->loadArchive(
                StringTmp<256>( "%s.szs", archive.cstr() ), nullptr );
}

void makeLocalizedArchivePath( sead::BufferedSafeString* out, const sead::SafeString& archive )
{
        out->format( "LocalizedData/%s/%s", al::getLanguage(), archive.cstr() );
}

void makeStageDataArchivePath( sead::BufferedSafeString* out, const char* stageName, int scenario, const char* type )
{
        out->format( "StageData/%s%s%d", stageName, type, scenario );
}

} // namespace al
```


