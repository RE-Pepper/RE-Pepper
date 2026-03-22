

# File alSensorFunction.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**LiveActor**](dir_8deca751c472e73f27f3806d878e75d2.md) **>** [**alSensorFunction.cpp**](al_sensor_function_8cpp.md)

[Go to the documentation of this file](al_sensor_function_8cpp.md)


```C++
#include <HitSensor/alHitSensor.h>
#include <LiveActor/alHitSensorKeeper.h>
#include <LiveActor/alLiveActor.h>
#include <LiveActor/alSensorFunction.h>
#include <Util/alStringUtil.h>

namespace alSensorFunction
{

struct NameToType
{
        const char*    name;
        al::SensorType type;
};

//NON_MATCHING

#define ALSENSORFUNCTION_ENTRY( TYPE ) { #TYPE, al::SensorType_##TYPE },

// clang-format off
const NameToType staticd(sNameToTypeLookupTable)[] = {
ALSENSORFUNCTION_ENTRY(Eye)
ALSENSORFUNCTION_ENTRY(Player)
ALSENSORFUNCTION_ENTRY(Npc)
ALSENSORFUNCTION_ENTRY(Ride)
ALSENSORFUNCTION_ENTRY(Enemy)
ALSENSORFUNCTION_ENTRY(EnemyBody)
ALSENSORFUNCTION_ENTRY(EnemyAttack)
ALSENSORFUNCTION_ENTRY(Dossun)
ALSENSORFUNCTION_ENTRY(KillerMagnum)
ALSENSORFUNCTION_ENTRY(EnemySimple)
ALSENSORFUNCTION_ENTRY(MapObj)
ALSENSORFUNCTION_ENTRY(MapObjSimple)
ALSENSORFUNCTION_ENTRY(Bindable)
ALSENSORFUNCTION_ENTRY(CollisionParts)
ALSENSORFUNCTION_ENTRY(KickKoura)
ALSENSORFUNCTION_ENTRY(PlayerFireBall)
ALSENSORFUNCTION_ENTRY(WooGanSandBody)
};
// clang-format on

#undef ALSENSORFUNCTION_ENTRY

#ifdef NON_MATCHING
al::SensorType findSensorTypeByName( const char* name )
{
        int            size = sizeof( sNameToTypeLookupTable ) / sizeof( sNameToTypeLookupTable[ 0 ] );
        al::SensorType type = al::SensorType_MapObj;
        for ( int i = 0; i < size; i++ )
        {
                if ( al::isEqualString( sNameToTypeLookupTable[ i ].name, name ) )
                {
                        // nop before beq
                        __nop();
                        type = sNameToTypeLookupTable[ i ].type;
                        break;
                }
        }
        return type;
}
#endif

void updateHitSensorsAll( al::LiveActor* actor )
{
        actor->getHitSensorKeeper()->update();
}

} // namespace alSensorFunction
```


