#include <Scene/SceneObjFactory.h>

// sub_15DF30, scene obj creator switch (unnamed in map)
static al::ISceneObj* fn_0015df30( int )
{
        return nullptr;
}

al::SceneObjHolder* SceneObjFactory::createSceneObjHolder()
{
        return new al::SceneObjHolder( fn_0015df30, SceneObj_Max );
}
