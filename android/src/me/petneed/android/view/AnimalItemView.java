package me.petneed.android.view;

import android.content.Context;
import android.util.AttributeSet;
import android.widget.FrameLayout;
import android.widget.ImageView;
import android.widget.TextView;
import com.googlecode.androidannotations.annotations.EViewGroup;
import com.googlecode.androidannotations.annotations.ViewById;
import com.koushikdutta.ion.Ion;
import me.petneed.android.R;
import me.petneed.android.model.Animal;
import me.petneed.android.model.DataManager;

@EViewGroup(R.layout.animal_view_item)
public class AnimalItemView extends FrameLayout {



	@ViewById(R.id.animal_image)
	protected ImageView img;
	@ViewById(R.id.animal_name)
	protected TextView name;

    public Animal getItem() {
        return mItem;
    }

    public void setItem(Animal mItem) {
        this.mItem = mItem;
    }

    private Animal mItem;


	public AnimalItemView(Context context) {
		super(context);
		init();
	}

	public AnimalItemView(Context context, AttributeSet attrs) {
		super(context, attrs);
		init();
	}

	public AnimalItemView(Context context, AttributeSet attrs, int defStyle) {
		super(context, attrs, defStyle);
		init();
	}
	
	private void init() {
		
	}

    public void bind(final Animal item) {
        setItem(item);

//        Ion.with(img)
//                .placeholder(R.drawable.empty_img)
//                .load(DataManager.STATIC_END_POINT+item.getImage_file());
        Ion.with(img)
                .placeholder(R.drawable.empty_img)
                .load(DataManager.STATIC_END_POINT+item.getImageFileThumb());
        name.setText(item.getName());

    }




}
