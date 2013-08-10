package me.petneed.android.model;

import android.content.Context;
import android.util.Log;
import com.google.gson.reflect.TypeToken;
import com.koushikdutta.async.future.FutureCallback;
import com.koushikdutta.ion.Ion;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Set;

/**
 * Created by Jacob Chen on 8/10/13.
 */
public class DataManager {


    public static final Object STATIC_END_POINT = "http://beta.petneed.me/static/media/";


    public int getTypeCount() {
        return data.size();
    }

    public Set<String> getTypes() {
        return data.keySet();
    }

    public List<Animal> getDataByType(String type) {
        if (data.get(type) != null)
            return data.get(type);
        else
            return new ArrayList<Animal>(); // should not happen XD
    }

    private HashMap<String, List<Animal>> data = new HashMap<String, List<Animal>>();

    private Context cxt;

    public DataUpdatedListener getListener() {
        return listener;
    }

    public void setListener(DataUpdatedListener listener) {
        this.listener = listener;
    }

    private DataUpdatedListener listener;

    public DataManager(Context _cxt) {
        cxt = _cxt;

    }


    public void initData() {




//        data.put("貓", new ArrayList<Animal>());
//        data.get("貓").add(new Animal("Lady","貓","http://petneed.me/static/media/28426141-f7c7-4092-a5ae-879dadce12bd_248x350.jpg"));
//        if (listener != null) {
//            listener.dataUpdated(ApiType.GET_ANIMALS);
//        }
        Ion.with(cxt, "http://beta.petneed.me/animal/API/0.1/animals/")
                .setLogging("MyLogs", Log.DEBUG)
                .as(new TypeToken<List<Animal>>() {
                })
                .setCallback(new FutureCallback<List<Animal>>() {
                    @Override
                    public void onCompleted(Exception e, List<Animal> animals) {
                        if (e != null){
                            if (listener != null){
                                listener.dataUpdateFailed(ApiType.GET_ANIMALS);
                            }
                            return;
                        }
                        for (Animal animal : animals){
                            //Animal animal = animalWrap.getFields();
                            if (data.get(animal.getType()) == null){
                                data.put(animal.getType(),new ArrayList<Animal>());
                            }
                            data.get(animal.getType()).add(animal);
                        }

                        if (listener != null){
                            listener.dataUpdated(ApiType.GET_ANIMALS);
                        }

                    }
                });
    }

    public Context getContext() {
        return cxt;
    }

    public enum ApiType {GET_ANIMALS}

    ;

    public interface DataUpdatedListener {

        public void dataUpdated(ApiType code);

        public void dataUpdateFailed(ApiType code);

        public void dataDetailView(Object obj);
    }
}
